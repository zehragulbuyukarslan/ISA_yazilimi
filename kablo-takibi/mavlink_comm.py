#mavlink_comm.py

from pymavlink import mavutil

class MavController:
    def __init__(self, device):
        self.master = mavutil.mavlink_connection(device, baud=115200)
        self.master.wait_heartbeat()
        print("Pixhawk bağlı:", self.master.target_system)

    def arm(self):
        self.master.arducopter_arm()
        print("ARM edildi.")

    def set_mode(self, mode):
        self.master.set_mode(mode)
        print(f"Mod ayarlandı: {mode}")

    def send_manual_control(self, x, y, z, r):
        self.master.mav.manual_control_send(
            self.master.target_system, x, y, z, r, 0
        )
