import os, shutil, winreg, ctypes, time, sys
try:
    from colorama import Fore
    import psutil
except ImportError:
    count = 0
    modules = ["colorama", psutil]
    for _ in modules:
        count += 1
        print(f"[INFO] Installing {_} | {count} / {len(modules)}")
        os.system(f"pip install {_} -q")
        print(f"[INFO] Successfully installed {_}\n")
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def info(msg: str) -> None:
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} {msg}")

def error(msg: str) -> None:
    print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.RESET} {msg}")

def warning(msg: str) -> None:
    print(f"{Fore.LIGHTYELLOW_EX}[INFO]{Fore.RESET} {msg}")

def success(msg: str) -> None:
    print(f"{Fore.LIGHTGREEN_EX}[INFO]{Fore.RESET} {msg}")

def verbose(msg: str) -> None:
    print(f"{Fore.LIGHTBLACK_EX}[INFO]{Fore.RESET} {msg}")

def pgisopen() -> bool:
    for proc in psutil.process_iter():
        if proc.name() == "Pixel Gun 3D.exe":
            try:
                return proc.pid > 0
            except:
                pass
    return False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

completed: int = 0
user_ids_str: str = ""

clear()
print("""Ban Trace Cleaner made by: YeetDisDude
This script does NOT unban you! This only reduces the chances of getting banned when you are creating a new account. It is recommended to use this script before you create a new account.\n""")
if pgisopen():
    error("Pixel Gun 3D is currently running! Close it and run the ban trace cleaner again.")
    input(f"\n{Fore.LIGHTWHITE_EX}[>>]{Fore.RESET} [{completed} / 2] Press enter to exit...")
    exit()

info(f"{Fore.LIGHTCYAN_EX}[1 / 2]{Fore.RESET} Removing {Fore.LIGHTCYAN_EX}LocalLow/Pixel Gun Team{Fore.RESET} directory...")
appdataDir = os.getenv("APPDATA")
if appdataDir == None:
    error("Error getting appdata path...  Exiting")
    input(f"\n{Fore.LIGHTWHITE_EX}[>>]{Fore.RESET} [{completed} / 2] Press enter to exit...")
    exit()
localLowDir = os.path.abspath(os.path.join(appdataDir, "..", "LocalLow"))
pgteamdir = localLowDir + "\Pixel Gun Team"
idDir = pgteamdir + "\\Pixel Gun 3D\\lobby_textures"
verbose(f"Pixel Gun Team Directory: {pgteamdir}")

if os.path.isdir(pgteamdir):
    verbose("Directory Exists! Deleting...")
    directories = os.listdir(idDir)
    user_ids = [int(d.split("-")[1]) for d in directories if d.startswith("user-")]
    user_ids_str = ", ".join(str(id) for id in user_ids)
    try:
        shutil.rmtree(pgteamdir)
        success("Deleted Pixel Gun Team!")
        completed += 1
    except Exception as e:
        error(f"Failed to delete directory, error: {e}")
else:
    error("This directory was not found, it may have been deleted already! Skipping...")

info(f"{Fore.LIGHTCYAN_EX}[2 / 2]{Fore.RESET} Removing {Fore.LIGHTCYAN_EX}Registry Keys{Fore.RESET}")
if is_admin() == 0:
    error("This script is not being ran with Administrator Privileges so it is unable to delete registery keys!")
    input(f"\n{Fore.LIGHTWHITE_EX}[>>]{Fore.RESET} [{completed} / 2] Press enter to exit...")
    exit()
else:
    try:
        pRemTarget = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Software" + "\\Pixel Gun Team")
        try:
            winreg.OpenKey(pRemTarget, "Pixel Gun 3D")
            winreg.DeleteKey(pRemTarget, "Pixel Gun 3D")
            success("Deleted Pixel Gun Team Registery keys!")
            completed += 1
        except:
            error("The registery keys were not found, it may have been deleted already! Skipping...")
            pass
    except Exception as e:
        error(f"Error when deleting keys: {e}")

print("\n")
success(f"Traces found: {user_ids_str}")
input(f"{Fore.LIGHTWHITE_EX}[>>]{Fore.RESET} [{completed} / 2] Finished cleaning ban traces! Press enter to exit...")