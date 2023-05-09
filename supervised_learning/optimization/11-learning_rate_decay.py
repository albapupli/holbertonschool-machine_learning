def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    updated_alpha = alpha / (1 + decay_rate * (global_step // decay_step))
    return updated_alpha
