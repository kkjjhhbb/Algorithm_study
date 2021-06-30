def solution(phone_book):
  phone_book.sort()
  answer = True
  for x,y in zip(phone_book, phone_book[1:]):
      if y.startswith(x):
          answer = False
          break
  return(answer)


def solution(phone_book):
    if len(phone_book) == 1:
        return False
    phone_book.sort()
    for prefix in phone_book:
        phone_book.remove(prefix)
        for phone_num in phone_book:
            if phone_num.startswith(prefix):
                return False
    return True
#효율성 3,4번 실패한 풀이