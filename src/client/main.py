import apihandler


apihandler.send_note("my thread", "my content", "my channel")

notes = apihandler.get_notes("my thread")
print(notes)