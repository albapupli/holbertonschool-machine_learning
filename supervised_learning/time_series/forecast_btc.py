#!/usr/bin/env python3
"""
Creates and trains a model to predict the value of Bitcoin
"""
import numpy as np
import pandas as pd
import tensorflow as tf


class WindowGenerator():
    """
    Create windows of consecutive data samples. 
    Windows are used to find trends within the data to make predictions. 
     - input_width: number of consecutive input time steps to use for each sample
     - label_width: number of time steps in the future to predict
     - shift: number of time steps between consecutive inputs      
    """
    def __init__(self, input_width, label_width, shift,
                 train_data, valid_data, test_data, label_columns=None):
        # set attributes with raw data
        self.train_data = train_data
        self.valid_data = valid_data
        self.test_data = test_data

        # label column indices
        self.label_columns = label_columns
        
        # dictionary that maps each column name to its corresponding index
        if label_columns is not None:
            self.label_columns_indices = {
                name: i for i, name in enumerate(label_columns)}
        # maps each column name to its corresponding index
        # easier for tensorflow to access by index
        self.column_indices = {
            name: i for i, name in enumerate(train_data.columns)}

        # window parameters
        self.input_width = input_width
        self.label_width = label_width
        self.shift = shift

        # the number of consecutive input time steps and horizon
        self.total_window_size = input_width + shift

        self.input_slice = slice(0, input_width)
        # generates an array of indices for the input window 
        self.input_indices = np.arange(
            self.total_window_size)[self.input_slice]

        # starting index for the label window within the total window size
        self.label_start   = self.total_window_size - self.label_width
        # a slice object representing the range of indices for the label window to the end
        self.labels_slice  = slice(self.label_start, None)
        # generates an array of indices corresponding to the label window
        self.label_indices = np.arange(
            self.total_window_size)[self.labels_slice]

    def split_window(self, features):
        """
        Converts list of consecutive inputs into window of inputs and
            window of labels
        """
        # extract the input and label windows from the provided features array, 
        # which represents a batch of consecutive input data.
        # The shape of this array is (batch_size, time_steps, num_features)
        inputs = features[:, self.input_slice, :]
        labels = features[:, self.labels_slice, :]
        
        if self.label_columns is not None:
            # construct a new tensor 
            # selecting all rows, and all time steps, then the
            # corresponding index of the desired label column
            labels = tf.stack(
                [labels[:, :, self.column_indices[name]] for
                 name in self.label_columns], axis=-1)

        # Slicing doesn't preserve static shape information, so set the shapes
        # manually. This way the `tf.data.Datasets` are easier to inspect.
        # allowing the tensors to accommodate varying batch sizes during training and evaluation
        inputs.set_shape([None, self.input_width, None])
        labels.set_shape([None, self.label_width, None])

        return inputs, labels

    def make_dataset(self, data):
        """
        Converts time series DataFrame into tf.data.Dataset
        """
        data = np.array(data, dtype=np.float32)
        ds = tf.keras.preprocessing.timeseries_dataset_from_array(
            data=data,
            targets=None,
            sequence_length=self.total_window_size,
            sequence_stride=1,
            shuffle=True,
            batch_size=32,)

        ds = ds.map(self.split_window)

        return ds

    @property
    def train(self):
        """
        Sets property to get tf.data.Dataset for training data
        """
        return self.make_dataset(self.train_data)

    @property
    def val(self):
        """
        Sets property to get tf.data.Dataset for validation data
        """
        return self.make_dataset(self.valid_data)

    @property
    def test(self):
        """
        Sets property to get tf.data.Dataset for testing data
        """
        return self.make_dataset(self.test_data)

    @property
    def example(self):
        """Get and cache an example batch of `inputs, labels` for plotting."""
        result = getattr(self, '_example', None)
        if result is None:
            # No example batch was found, so get one from the `.train` dataset
            result = next(iter(self.train))
            # And cache it for next time
            self._example = result
        return result


def compile_and_fit(model, window, patience=2, epochs=20):
    """
    Compiles and fits the model to return history
    """
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                      patience=patience,
                                                      mode='min')

    model.compile(loss=tf.losses.MeanSquaredError(),
                  optimizer=tf.optimizers.Adam(),
                  metrics=[tf.metrics.MeanAbsoluteError()])

    history = model.fit(window.train, epochs=epochs,
                        validation_data=window.val,
                        callbacks=[early_stopping])
    return history


def time_series_forecasting(train, valid, test):
    """
    Creates and trains a model to predict the value of Bitcoin

    parameters:
        train: preprocessed training dataset
        valid: preprocessed validation dataset
        test: preprocessed testing dataset
    """
    window = WindowGenerator(input_width=24, label_width=1, shift=1,
                             train_data=train, valid_data=valid,
                             test_data=test, label_columns=['Close'])

    lstm_model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(24, return_sequences=False),
        tf.keras.layers.Dense(units=1)
    ])

    history = compile_and_fit(lstm_model, window)

    # Make predictions on the test dataset
    test_performance = {}
    test_performance['LSTM'] = lstm_model.evaluate(window.test)

    # Get the example batch from the test dataset for predictions
    inputs, targets = next(iter(window.test))

    # Make predictions using the trained model
    predictions = lstm_model.predict(inputs)

    # Plot the actual values and the predicted values
    plt.plot(np.arange(len(targets[0])), targets[0], label='Actual')
    plt.plot(np.arange(len(predictions[0])), predictions[0], label='Predicted', linestyle='dashed')
    plt.xlabel('Time')
    plt.ylabel('Bitcoin Close Value')
    plt.title('Bitcoin Price Forecasting with LSTM')
    plt.legend()
    plt.show()

    return test_performance

if __name__ == '__main__':
    train_data, valid_data, test_data = preprocess_data()
    test_performance = time_series_forecasting(train_data, valid_data, test_data)
