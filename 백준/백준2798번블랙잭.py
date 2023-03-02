n, m = map(int, input().split())
card = list(map(int, input().split()))

blackjack = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] <= m:
                blackjack.append(card[i] + card[j] + card[k])
print(max(blackjack))