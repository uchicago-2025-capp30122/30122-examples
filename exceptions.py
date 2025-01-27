# TODO: copy example to repo
try:
    1 / 2
except ValueError as e:
    print("got a value error:", e)
except Exception as e:
    print("got some other error:", type(e), e)
else:
    print("else executed")
finally:
    print("always prints at the end")
