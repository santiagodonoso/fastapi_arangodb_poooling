USER_NAME_MIN_LEN = 2
USER_NAME_MAX_LEN = 20


def validate_user_name(text):
  text = text.strip()
  text = " ".join(text.split())
  if len(text) < USER_NAME_MIN_LEN: return False
  if len(text) > USER_NAME_MAX_LEN: return False
  return text


def validate_from_to(start, limit):
  if int(start) > int(limit):
    return False, False
  return start, limit