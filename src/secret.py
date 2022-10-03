from dataclasses import dataclass


@dataclass
class Secrets:
    sender_email: str = "rons.robots@gmail.com"
    sender_password: str = "pdsngwgsupylfmot"
    receiver_email: str = "ronaldlussier83@gmail.com, rons.robots@gmail.com"
