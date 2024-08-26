import psutil
import time
import ctypes

class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    GRAY = '\033[90m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

process_name = 'GTA5.exe'
process_id = 777

# Find the process ID of the process
for proc in psutil.process_iter():
    if process_name in proc.name():
        process_id = proc.pid
        break

# Quit if process not found.
if process_id == 777:
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Gta V process not found. You sure game is running?', 'Oh...', 0)
    quit()


print()
print()
print(f"  {colors.GRAY}▄▀▀▀▀▄   ▄▀▀▀█▀▀▄  ▄▀▀█▄     {colors.GREEN}  ▄▀▀▄  ▄▀▀▄  {colors.GRAY}    ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ")
print(f"  {colors.GRAY}█        █    █  ▐ ▐ ▄▀ ▀▄   {colors.GREEN}  █   █     █ {colors.GRAY}   █ █   ▐ █    █  ▐ █      █ █   █   █ ")
print(f"  {colors.GRAY}█    ▀▄▄ ▐   █       █▄▄▄█   {colors.GREEN}  ▐  █     █  {colors.GRAY}      ▀▄   ▐   █     █      █ ▐  █▀▀▀▀  ")
print(f"  {colors.GRAY}█     █ █   █       ▄▀   █   {colors.GREEN}     █   ▄▀   {colors.GRAY}   ▀▄   █     █      ▀▄    ▄▀    █      ")
print(f"  {colors.GRAY}▐▀▄▄▄▄▀ ▐ ▄▀       █   ▄▀    {colors.GREEN}      ▀▄▀     {colors.GRAY}    █▀▀▀    ▄▀         ▀▀▀▀    ▄▀       ")
print(f"  {colors.GRAY}▐        █         ▐   ▐     {colors.GREEN}              {colors.GRAY}    ▐      █                  █         ")
print(f"  {colors.GRAY}         ▐                   {colors.GREEN}              {colors.GRAY}           ▐                  ▐         ")
print()
print()

# Find him.
process = psutil.Process(process_id)
print(f"    {colors.GRAY}[{time.strftime("%H:%M:%S", time.localtime())}] {colors.WHITE}fac.e {colors.GRAY}>>{colors.WHITE} I found the {colors.RED}target {colors.WHITE}with PID ({process.pid}).")

# Stop his heart.
process.suspend()
print(f"    {colors.GRAY}[{time.strftime("%H:%M:%S", time.localtime())}] {colors.WHITE}fac.e {colors.GRAY}>>{colors.WHITE} I'm stopping the heart of {colors.RED}{process_name}")

time.sleep(8)

# Show some mercy and let him live.
process.resume()
print(f"    {colors.GRAY}[{time.strftime("%H:%M:%S", time.localtime())}] {colors.WHITE}fac.e {colors.GRAY}>>{colors.WHITE} Resuming! Have fun in your sad and empty session >:(")


time.sleep(2)
