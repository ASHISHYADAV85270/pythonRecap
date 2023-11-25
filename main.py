import  os

if __name__ == '__main__':
    print("welcome to RoboSpeaker 1.1. Created By Ashish")
    x=input("Enter what u want me to pronounce: ")
    try:
        command=f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
        os.system(command)
    except:
        print("some errro")
