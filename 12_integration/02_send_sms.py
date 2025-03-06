import vonage

client = vonage.Client(key="0a716bba", secret="mvme7GBv3lngVDxA")
sms = vonage.Sms(client)

responseData = sms.send_message({
    "from": "test",
    "to": "",
    "text": "this sms send with python application"
})

if responseData["messages"][0]["status"] == "0":
    print("send your message")
else:
    print(f"error: ", {responseData['messages'][0]['error-text']})