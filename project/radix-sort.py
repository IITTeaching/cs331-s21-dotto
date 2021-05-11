import urllib.request
def radix(arr):
  n = len(arr)
  maxL = len(max(arr, key = len))
  for d in reversed(range(maxL)):
    count = [0] * 128
    output = [''] * n
    for i in range(n):
      count[arr[i][d] + 1] += 1
    for k in range(1, 128):
      count[k] += count[k-1]
    for j in range(n):
      output[count[arr[j][d]]] = arr[j]
      count[arr[j][d]] += 1
    for m in range(n):
      arr[m] = output[m]
  return output
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()
def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    arr = book_to_words()
    maxL = len(max(arr, key = len))
    for i in range(len(arr)):
        arr[i] = arr[i].decode('ascii')
        if len(arr[i]) < maxL:
            while len(arr[i]) < maxL:
                arr[i] = arr[i] + '!'
        arr[i] = bytes(arr[i], encoding='ascii')
    radix(arr)
    for i in range(len(arr)):
        arr[i] = arr[i].decode('ascii')
        arr[i] = arr[i].replace('!', '')
        arr[i] = bytes(arr[i], encoding='ascii')
    return arr
###print (radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'))
### ^main
