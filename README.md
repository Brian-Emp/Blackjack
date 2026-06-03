# 🃏 The Blackjack

A simple command-line **Blackjack** game written in Python. Place a bet, draw cards against the dealer, and try to beat them without going over 21!

> ⚠️ The game interface is in **French** (prompts and messages).

---

## 🎮 Gameplay

1. Enter your username and your bet.
2. You're dealt a card, then the dealer is dealt one.
3. On each turn, choose to **hit** (`1`) or **stand** (`2`).
4. When you stand, the dealer draws until reaching at least **17**.
5. Outcomes are resolved according to standard Blackjack rules.

### Rules implemented

- **Card values:** 2–10 at face value, face cards (Jack, Queen, King) worth 10, Ace worth 11.
- **Blackjack (21):** you win **1.5×** your bet plus your stake back.
- **Bust (> 21):** you lose your bet immediately.
- **Dealer busts:** you win your bet.
- **Higher score than the dealer (≤ 21):** you win your bet.
- **Tie:** your bet is returned (push).
- **Lower score than the dealer:** you lose your bet.

---

## 🚀 Run it

You only need Python 3 — no external dependencies (uses the standard `random` module).

```bash
git clone https://github.com/Brian-Emp/Blackjack.git
cd Blackjack
python BJack.py
```

---

## 📂 Project structure

```
Blackjack/
├── .gitattributes
└── BJack.py        # Full game logic
```

---

## 🛠️ Built with

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📌 Notes & possible improvements

- The deck draws cards randomly with replacement (cards aren't removed from a finite deck).
- Aces are always counted as 11 (no automatic soft/hard Ace adjustment).
- Ideas for future versions: tracking a persistent balance, multiple rounds, a proper 52-card deck, soft-Ace handling, and an English language option.

---

> Made by [Brian-Emp](https://github.com/Brian-Emp) 
