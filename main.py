from view.acceptance_view import *
from view.admin_view import *
from view import *


def main_app():
    AcceptanceView("Acceptance View", "1200x480", open_Car_wash_command=open_car_wash)


def open_car_wash(current_view):
    current_view.destroy_window()
    CarWashView("CarWash View", "600x400")
    main_app()

    # AcceptanceView("autoservice View", "1000x410")
    # AdminView("Admin", "600x300")

    # def open_Acceptance(current_view):
    #     current_view.destroy_window()
    #     AcceptanceView("Acceptance View", "1200x800")


    # def repairs(current_view):
    #     current_view.destroy_window()
    #     RepairsView("Repairs", "700x350")
    #     main_app()


    # def open_Admin(current_view):
    #     current_view.destroy_window()
    #     AdminView("Admin view", "45x300")
    #     main_app()
    #
    #


main_app()
