def flightbookings(bookings, n):
    answers = [0] * n
    for booking in bookings:
        first, last, seat = booking
        answers[first-1] += seat
        if last < n:
            answers[last] -= seat   

    for i in range(1, n):
        answers[i] += answers[i-1]

    return answers

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(flightbookings(bookings, n))

