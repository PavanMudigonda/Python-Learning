# String segmentation
def can_segment_string(s, dictionary):
  #TODO: Write - Your - Code
  for i in range(1, len(s)+1):
    first=s[:i]
    if first in dictionary:
      second=s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False



can_segment_string('hellonow',set(["hello","hell","on","now"]))