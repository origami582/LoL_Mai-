#จับเสียงพูด
import speech_recognition as sr
#ใช้ในการรันคำสั่งในระบบปฏิบัติการ
import subprocess
RIOT_CLIENT = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
COMMANDS = {
    "แอลไหม": [
        RIOT_CLIENT,
        "--launch-product=league_of_legends",
        "--launch-patchline=live"
    ],
    "เอาไหม": [
        RIOT_CLIENT,
        "--launch-product=league_of_legends",
        "--launch-patchline=live"
    ],
}

recognizer = sr.Recognizer()
mic = sr.Microphone()


def riot_is_running():
    tasks = subprocess.check_output("tasklist", shell=True).decode()
    return "RiotClientServices.exe" in tasks

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="th-TH")
        print(f"คุณพูดว่า: {text}")

        for command, path in COMMANDS.items():
            if command in text:
                if not riot_is_running():
                    subprocess.Popen(path)

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass