---
layout: post
title: Probabilities - Mill & Draw CXs
author: Shoty
date: 2026-04-08
permalink: blog/probabilities-mill-and-draw-cx/
description: Common probabilities for milling or drawing that you would often encounter in Weiss Schwarz.
---

### Contents:
- [Introduction](#introduction)
- [Brainstorm](#brainstorm)
- [Mill 3](#mill-3)
- [Drawing CXs](#drawing-cxs)
- [Concluding Remarks](#concluding-remarks)
- [Assumptions](#assumptions)

## Introduction {#introduction}
In this post I will be sharing probabilities of various draws and mills involving CXs that you will often encounter in Weiss Schwarz. Examples of this includes chances of hitting brainstorm on deck 1, milling CXs off your advantage combo, or drawing the right CXs by turn 2. These are all examples of hypergeometric distributions and all numbers you see below are calculated with the help of the calculator from [**StatTrek**](https://stattrek.com/online-calculator/hypergeometric).

This is more of an education post and the goal is to help intermediate players, who are looking to improve their gameplay competitively, make more informed decisions by knowing the probabilities behind their actions. Being more aware of the various chances can help you better judge how lucky or unlucky you were, and allow you to take more objective notes on when variance favored you or your opponent. Tracking your own statistics is a great way to find a path towards improvement, please check out Beanwolf's post about [**Variance, Mindset & other Delusions**](https://thebeanwolf.blogspot.com/2022/06/variance-mindset-other-delusions.html) for a more in-depth discussion of that. 

### Preface
In each section I will first present the relevant data, followed by an insights section to share any interesting observations. While the insights section would cover many common questions that a Weiss player might have, I urge you to take a close look at the data yourself.

- For deck 1 I will use `8 in 50` for all probabilities.<br>
- For deck 2 I will use `8 in 30` and `7 in 30`.
    - This is after taking into account that there are 5 cards on board, 6 cards in hand, 4 cards in stock, 4 cards in clock, and 1 card in level after refresh. 
    - Not every deck 2 will have be in this configuration, sometimes you'll be more compressed or less compressed. I found that this is a sufficient average to benchmark deck 2 with.

If you need convincing as to why I use `8 in 50` for the deck 1 then please read the ["Assumptions"](#assumptions) section.

## Brainstorm {#brainstorm}
Brainstorm is the most common form of mill, and arguably the most important form of mill so we will start with it.<br>

#### Deck 1

| 8 in 50      | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 | x = 4 |
| ------------ | ----- | ----- | -----:| -----:| -----:| -----:|
| Brainstorm 4 | 51.4% | 11.6% | 39.9% | 10.5% | 1.02% | 0.03% |
| Brainstorm 5 | 59.9% | 17.6% | 42.3% | 15.2% | 2.28% | 0.14% |
| Brainstorm 6 | 67.0% | 24.2% | 42.8% | 19.7% | 4.05% | 0.38% |
| Double-bs 4  | 78.0% | 37.8% | 40.2% | 27.4% | 8.87% | 1.46% |
{: .bold-third-right .no-wrap}

<sup>\* To calculate the probability of hitting 3 or more (x ≥ 3) simply sum up everything from the x=3 column to the right (ie. x=3 and x=4).</sup>

#### Deck 2

| 8 in 30      | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 | x = 4 |
| -----------  | ----- | ----- | -----:| -----:| -----:| -----:|
| Brainstorm 4 | 73.3% | 28.4% | 45.0% | 23.6% | 4.50% | 0.26% |
| Brainstorm 5 | 81.5% | 40.5% | 41.1% | 30.3% | 9.08% | 1.08% |
| Brainstorm 6 | 87.4% | 52.0% | 35.5% | 34.5% | 14.5% | 2.72% |
| Double-bs 4  | 94.5% | 71.2% | 23.3% | 35.7% | 25.2% | 8.75% |
{: .bold-third-right .no-wrap}

| 7 in 30      | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 | x = 4 |
| -----------  | ----- | ----- | -----:| -----:| -----:| -----:|
| Brainstorm 4 | 67.7% | 22.5% | 45.2% | 19.4% | 2.94% | 0.13% |
| Brainstorm 5 | 76.4% | 32.9% | 43.5% | 26.1% | 6.21% | 0.56% |
| Brainstorm 6 | 83.0% | 43.3% | 39.7% | 31.3% | 10.5% | 1.49% |
| Double-bs 4  | 91.6% | 62.3% | 29.3% | 36.2% | 20.1% | 5.30% |
{: .bold-third-right .no-wrap}

Why do so many experienced players say that getting to deck 2 is important? Hopefully these tables can demonstrate that quantitatively.

#### Extreme Deckstates w/ Brainstorm 4

| Brainstorm 4 | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 | x = 4 |
| -----------  | ----- | ----- | -----:| -----:| -----:| -----:|
| 6 in 12      | 97.0% | 72.7% | 24.2% | 45.5% | 24.2% | 3.03% |
| 2 in 12      | 57.6% | 9.09% | 48.5% | 9.09% |       |       |
| 1 in 12      | 33.3% |       | 33.3% |       |       |       |
| 4 in 30      | 45.5% | 7.50% | 38.0% | 7.12% | 0.38% |       |
{: .bold-third-right .no-wrap}

I picked several `x in 12` because there are important decision points when reaching the end of your deck. Hopefully these are enough to represent the different scenarios.<br>
As for `4 in 30` it's to represent a "poor" deck 2.

#### Insights
- The chances of hitting brainstorm 4 on deck 1 is practically a coinflip (**51.4%**), while the odds is increased significantly in your favor in deck 2 (**73.3%**) - over 40% more likely.
- Brainstorm 5 gains significant value over brainstorm 4 in deck 2, with the chances of hitting 2 or more CXs being slightly above **40%** vs **30%** - a third more likely.
- For all you double brainstorm enjoyers out there the chances to whiff on deck 1 is more than **20%**, that means that you'll whiff approximately once every 5 games. Conversely, on deck 2 the chance to whiff is actually not that low at **5.5%**, that's almost the double the rate of hitting an SSR in UmaMusume, beware!

- Even in a "poor" deck 2 of `4 in 30` the chances of hitting a brainstorm 4 is still close to a coinflip at **45.5%**, demonstrating the power of deck 2 compression.
- In a deck that's `6 in 12`, the chances of hitting 2 or more CXs is quite high at **72.7%**. However, this also means that there is a **27.3%** chance that you will hit 1 or less CXs and is left dealing with a deck that is `5 in 8`. 

<sup>**NOTE:** You can use the "Brainstorm 4" values for other common mill 4 effects such as [**Torch**](https://en.ws-tcg.com/cardlist/?cardno=GBS/S63-TE08), [**Akatsuki**](https://en.ws-tcg.com/cardlist/?cardno=KC/S31-E040), [**Amagi**](https://en.ws-tcg.com/cardlist/?cardno=KC/S42-E001), or [**Maguro**](https://heartofthecards.com/code/cardlist.html?card=WS_PY/S38-096) too, though knowing the number of CXs milled is not as important here.</sup>

## Mill 3 {#mill-3}
A lot of actions in Weiss has to do with milling 3, most commonly by attacking 3 times or draw-clock-draw2. Some examples other examples includes: [**Koume-3**](https://heartofthecards.com/code/cardlist.html?card=WS_IMC/W43-086), [**Lv1 Itsuki-variants**](https://en.ws-tcg.com/cardlist/?cardno=5HY/W90-E050), [**Tornado event**](https://en.ws-tcg.com/cardlist/?cardno=AB/W31-E098), etc. Knowing the probabilities of seeing CXs for these scenarios are all very important since you're looking to plus, get selection, or dig for a CX.

| Mill 3               | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 |
| -------------------- | ----- | ----- | -----:| -----:| -----:|
| 8 in 50 (Deck 1)     | 41.4% | 6.29% | 35.1% | 6.00% | 0.29% |
| 8 in 30 (Deck 2)     | 62.1% | 16.6% | 45.5% | 15.2% | 1.38% |
| 7 in 30 (Deck 2)     | 56.4% | 12.8% | 43.6% | 11.9% | 0.86% |
| 6 in 12 (Compressed) | 90.9% | 50.0% | 40.9% | 40.9% | 9.09% |
{: .bold-third-right .no-wrap}

| Mill 3x2             | x ≥ 1 | x ≥ 2 | x = 1 | x = 2 | x = 3 |
| -------------------- | ----- | ----- | -----:| -----:| -----:|
| 8 in 50 (Deck 1)     | 67.0% | 24.2% | 42.8% | 19.7% | 0.38% |
| 8 in 30 (Deck 2)     | 87.4% | 51.9% | 35.5% | 34.5% | 14.5% |
| 7 in 30 (Deck 2)     | 83.3% | 43.3% | 39.7% | 31.3% | 10.4% |
| 6 in 12 (Compressed) | 99.9% | 96.0% | 3.90% | 24.4% | 43.3% |
{: .bold-third-right .no-wrap}

#### Insights
- Tri-laning is close to coin flip whether you'll trigger in deck 1 at **41.4%**, then in deck 2 it is more favored at **62.1%**.
- Similar to the above, when looking for a CX on deck 1, clock-draw will get you at least one **41.4%** of the time. However, if you didn't get a CX and needed to use a Koume-3 to dig for one, the chances of success for the entire interaction is only **67.0%** - this means that you'll fail to get a CX approximately a third of the time.

- When swinging three times on a super compressed deck state (6 in 12) you're not more unlikely to trigger 2 CXs over 1 - they are both **40.9%** each respectively. Meanwhile, there's a **~9%** chance to triple trigger, and the same chance to not trigger at all.

- The chances of plussing 2 on Itsuki combo is pretty good on Deck 1 at almost **60%**, but from deck 2 and onwards it starts to become worse than coinflip. The chances of milling 2 CXs to go even is also quite high at over **16.6%** on deck 2.
    - In this scenario it might be more useful to look at the mean - the expected number of CXs you'll mill. Following is the mean for triple Itsuki (mill 9).

        | Mill 3 x 3 | 8 in 50 | 8 in 30 | 7 in 30 |
        | ---------- | ------- | ------- | ------- |
        | Mean       | 1.44    | 2.4     | 2.1     |
    - Reading the above table we can expect to +5 off triple Itsuki in deck 1. On deck 2, however, the expectation should be lowered to only be +4.

## Drawing CXs {#drawing-cxs}
This section will show the chances of drawing CXs over the first two turns of the game. 

- I will provide data for drawing **11** cards (0 mulligan) up to drawing **16** cards (full 5 mulligan).
    - After drawing 5 for turn and clock-drawing for 2 turns there is a total of **11** cards drawn, this number is the same regardless of whether you're going 1st or 2nd.

I will not be taking into account triggers or damage taken because in a randomized deck their individual probabilities does not affect the overall probability of draw. 

#### Drawing the correct CX (4 successes)

| # of Draws  | x ≥ 1 | x ≥ 2 | Mean  | x = 1 | x = 2 | x = 3 |
| ----------- | ----- | ----- | ----- | -----:| -----:| -----:|
| 11 (Mull 0) | 64.3% | 20.6% | 0.88  | 43.7% | 17.7% | 2.79% |
| 12 (Mull 1) | 67.9% | 24.0% | 0.96  | 43.0% | 20.2% | 3.63% |
| 13 (Mull 2) | 71.3% | 27.5% | 1.04  | 43.9% | 22.6% | 4.59% |
| 14 (Mull 3) | 74.4% | 31.0% | 1.12  | 43.4% | 24.9% | 5.69% |
| 15 (Mull 4) | 77.3% | 34.6% | 1.20  | 42.6% | 27.1% | 6.91% |
| 16 (Mull 5) | 79.9% | 38.3% | 1.28  | 41.6% | 29.2% | 8.27% |
{: .bold-fourth-right .no-wrap}

#### Drawing any CXs (8 successes)

| # of Draws  | x ≥ 1 | x ≥ 2 | x ≥ 3 | Mean  | x = 1 | x = 2 | x = 3 | x = 4 |
| ----------- | ----- | ----- | ----- | ----- | -----:| -----:| -----:| -----:|
| 11 (Mull 0) | 88.5% | 57.0% | 23.6% | 1.76  | 31.5% | 33.4% | 17.7% | 5.06% |
| 12 (Mull 1) | 90.9% | 62.7% | 28.7% | 1.92  | 28.2% | 33.9% | 20.6% | 6.81% |
| 13 (Mull 2) | 92.8% | 67.9% | 34.1% | 2.08  | 24.9% | 33.8% | 23.2% | 8.80% |
| 14 (Mull 3) | 94.4% | 72.6% | 39.6% | 2.24  | 21.8% | 33.0% | 25.6% | 11.0% |
| 15 (Mull 4) | 95.6% | 76.8% | 45.1% | 2.40  | 18.8% | 31.7% | 27.5% | 13.3% |
| 16 (Mull 5) | 96.6% | 80.6% | 50.5% | 2.56  | 16.0% | 30.0% | 29.0% | 15.7% |
{: .bold-fifth-right .no-wrap}

#### Insights
- The chances of drawing the correct CX for level 1 combo is quite high at **74.4%** after a typical mulligan 3 - you'll only miss the CX about one in every 4 games.
- There's some diminishing return for mulligan. A mulligan for 0 vs 2 gives a **7%** increase, while a mulligan for 3 vs 5 gives **5.5%**.
    - Realistically there are other more important factors at play during mulligan before this becomes a consideration. 
    <br><br>
- By turn 2 you can expect to see any **2** CXs on average, so it's worthwhile to be prepared and know what to do with a spare CX for every game. 
- Getting flooded by 3 or more CXs in hand is not that unlikely at **34.1%** after a typical mulligan for 2 - it is **10.9%** for 4 or more. It might be worthwhile to consider this during deckbuilding to make sure that there are ditch-outs in case things go south.
    - By the way, ditching a CX off mulligan doesn't mean that the chances of drawing more CXs has decreased. The **10.9%** chance of seeing 4 or more CXs after drawing 13 cards is fixed regardless of whether you ditched one or two CXs off mulligan.

## Concluding Remarks {#concluding-remarks}
Game's all luck. text text text

## Assumptions {#assumptions}
This section is not part of the main article. Here, I will explain why `8 in 30` is used for the first deck instead of something more realistic like `7 in 40`.

Let's use a standard brainstorm 4 as an example, we get the following probabilties in a brand new deck.

| Brainstorm 4 | x ≥ 1 | x = 1  | x = 2  | x = 3  | x = 4  |
| -----------  | ----- | ------ | ------ | ------ | ------ |
| 8 in 50      | 51.4% |  39.9% | 10.5%  | 1.02%  | 0.03%  | 

For comparison, here are the probabilities after performing a mulligan for 2 and clock drawing (5 + 2 + 1+ 2 = 10 cards). The percentages under the first column are the chances to arrive to that deck state after drawing 10 cards.

| Brainstorm 4 | x ≥ 1 | x = 1 | x = 2 | x = 3 | x = 4 |
| ------------ | ----- | ----- | ----- | ----- | ----- |
| 8 in 40 (14%)| 60.7% | 43.4% | 15.2% | 1.96% | 0.08% |
| 7 in 40 (35%)| 55.2% | 41.8% | 12.1% | 1.26% | 0.04% | 
| 6 in 40 (32%)| 49.2% | 39.3% | 9.21% | 0.74% | 0.02% | 
| 5 in 40 (15%)| 42.7% | 35.8% | 6.51% | 0.38% | 0.01% | 

Doing some quick maths for the probabilities of hitting one or more CXs we have: `60.7*0.14 + 55.2*0.35 + 49.2*0.32 + 42.7*0.15 = 49.97%`, this is very close to the probability for `8 in 50`. In fact, this is a conservative estimate because we are missing the probabilities for 3, 2, and 1 CXs in deck, which you'll find will add up to the original 51.4%. I hope that this is convincing enough to go ahead with using `8 in 50` for deck 1 probabilities. 
