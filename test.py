import speedtest
speed=speedtest.Speedtest()
download_speed=speed.download()
upload_speed=speed.upload()
print(f"download speed:{download_speed}")
print(f"upload speed:{upload_speed}")

