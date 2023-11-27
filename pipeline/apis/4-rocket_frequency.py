#!/usr/bin/env python3

"""
By using the (unofficial) SpaceX API, write a script that displays the number of launches per rocket.

Use this https://api.spacexdata.com/v3/launches to make request
All launches should be taking in consideration
Each line should contain the rocket name and the number of launches separated by : (format below in the example)
Order the result by the number launches (descending)
If multiple rockets have the same amount of launches, order them by alphabetic order (A to Z)
Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)
"""

"""
By using the (unofficial) SpaceX API, write a script that displays the number
of launches per rocket.
"""

import requests

if __name__ == "__main__":
    url_launches = 'https://api.spacexdata.com/v4/launches'
    launches = requests.get(url_launches).json()

    rocket_dict = {}

    for launch in launches:
        rocket_id = launch.get('rocket')
        url_rocket = 'https://api.spacexdata.com/v4/rockets/{}'.format(
            rocket_id
        )
        rocket_info = requests.get(url_rocket).json()
        rocket_name = rocket_info.get('name')

        if rocket_dict.get(rocket_name) is None:
            rocket_dict[rocket_name] = 1
            continue
        rocket_dict[rocket_name] += 1

    sorted_rocket = sorted(rocket_dict.items(),
                           key=lambda kv: kv[1],
                           reverse=True)

    for rocket, count in sorted_rocket:
        print("{}: {}".format(rocket, count))
