---
layout: post
title: Probabilities - Mill & Draw
author: Shoty
date: 2026-02-26
permalink: blog/probabilities-mill-and-draw/
description: Common probabilities for milling or drawing that you would often encounter in Weiss Schwarz.
---

### Contents:
- [Introduction](#introduction)
- [Brainstorm](#brainstorm)
- [Mill](#mill)
- [Plussing Zeros](#plussing-zeros)

## Introduction {#introduction}
In this post I will be sharing probabilities of draw/mill events you will often encounter in Weiss Schwarz. Examples of this includes chances of hitting brainstorm on deck 1, chances of missing aqua riki on deck 1, chances of drawing the right cxs by turn 2, etc. These are all examples of hypergeometric distributions and all numbers you see below are calculated with the help of the calculator from [**StatTrek**](https://stattrek.com/online-calculator/hypergeometric).

The goal of this post is help intermediate players, who are looking to improve their gameplay competitively, make more informed decisions by knowing the probabilities behind their actions. Being more aware of this can also help you accurately determine how lucky or unlucky you got, and be able to take objective notes of when the variance went your way or your opponent's way. Tracking your own statistics is a great way to find a path towards improvement, please check out Beanwolf's post about [**Variance, Mindset & other Delusions**](https://thebeanwolf.blogspot.com/2022/06/variance-mindset-other-delusions.html) for a more in-depth discussion of that. 

### Assumptions
I will be using `8 in 50` for all deck 1 probabilities.
For deck 2 I will be using `8 in 30`. This is after taking into account that there are 5 cards on board, 6 cards in hand, 4 cards in stock, 4 cards in clock, and 1 card in level. Not every deck 2 will have this probability, sometimes you'll be more compressed or less compressed. I found that this is a sufficient average to benchmark deck 2 with.

If you need convincing as to why I use those deck states and not something more realistic like `7 in 40` or `4 in 25`, etc then I will try to clear that up below. Otherwise, feel free to skip past and jump down to the various sections.

Let's use a standard brainstorm 4 as an example, we get the following probabilties in a brand new deck.

| Brainstorm 4 | x ≥ 1 | x = 1  | x = 2  | x = 3  | x = 4  |
| -----------  | ----- | ------ | ------ | ------ | ------ |
| 8 in 50      | 51.4% |  39.9% | 10.5%  | 1.02%  | 0.03%  | 

For comparison, here are the probabilities after performing a mulligan for 2 and clock drawing (5 + 2 + 1+ 2 = 10 cards). The percentages next to the first column is the chances to arrive to that deck state after drawing 10 cards.

| Brainstorm 4 | x ≥ 1 | x = 1 | x = 2 | x = 3 | x = 4 |
| ------------ | ----- | ----- | ----- | ----- | ----- |
| 8 in 40 (14%)| 60.7% | 43.4% | 15.2% | 1.96% | 0.08% |
| 7 in 40 (35%)| 55.2% | 41.8% | 12.1% | 1.26% | 0.04% | 
| 6 in 40 (32%)| 49.2% | 39.3% | 9.21% | 0.74% | 0.02% | 
| 5 in 40 (15%)| 42.7% | 35.8% | 6.51% | 0.38% | 0.01% | 

Doing some quick maths for the probabilities of hitting one or more cxs `60.7*0.14 + 55.2*0.35 + 49.2*0.32 + 42.7*0.15 = 49.97%`, this is very close to the probability for 8 in 50. In fact, this is a conservative estimate because we are missing the probabilities for 3, 2, and 1 in deck, which you'll find will add up to the original 51.4%. I hope that this is convincing enough to go ahead with using `8 in 50` for deck 1 probabilities, and `8 in 30` for deck 2. 

## Brainstorm {#brainstorm}
Brainstorm is the most common form of mill, and arguably the most important form of mill so I will start with it.<br>
*<sup>I know that there's literally only one way to perform a brainstorm 6 at the time of this writing, it's there for myself.</sup>*

**Deck 1**

| 8 in 50      | x ≥ 1 | x = 1  | x = 2  | x = 3  | x = 4  |
| -----------  | ----- | ------ | ------ | ------ | ------ |
| Brainstorm 4 | 51.4% |  39.9% | 10.5%  | 1.02%  | 0.03%  |
| Brainstorm 5 | 59.9% |  42.3% | 15.2%  | 2.28%  | 0.14%  |
| Brainstorm 6 | 67.0% |  42.8% | 19.7%  | 4.05%  | 0.38%  |
| Double BS 4  | 78.0% |  40.2% | 27.36% | 8.87%  | 1.46%  |

For something like double brainstorm 4 knowing the probability of hitting 2 or more (x ≥ 2) is probably more useful, to know this simply sum up everything from the x=2 column to the right (ie. x=2, x=3, and x=4)

**Deck 2**

| 8 in 30      | x ≥ 1 | x = 1  | x = 2  | x = 3  | x = 4  |
| -----------  | ----- | ------ | ------ | ------ | ------ |
| Brainstorm 4 | 73.3% |  45.0% | 23.6%  | 4.50%  | 0.26%  |
| Brainstorm 5 | 81.5% |  41.1% | 30.3%  | 9.08%  | 1.08%  |
| Brainstorm 6 | 87.4% |  35.5% | 34.5%  | 14.5%  | 2.10%  |
| Double BS 4  | 94.5% |  23.3% | 35.7%  | 25.2%  | 8.75%  |

Why do so many experienced players say that getting to deck 2 is important? Hopefully this table can demonstrate that quantitatively.

**Extreme Deckstates w/ Brainstorm 4**

| Brainstorm 4 | x ≥ 1 | x = 1  | x = 2  | x = 3  | x = 4  |
| -----------  | ----- | ------ | ------ | ------ | ------ |
| 6 in 12      | 97.0% |  24.2% | 45.5%  | 24.2%  | 3.03%  |
| 2 in 12      | 57.6% |  48.5% | 9.09%  |        |        |
| 1 in 12      | 33.3% |  33.3% |        |        |        |
| 4 in 30      | 45.5% |  38.0% | 7.12%  | 0.38%  |        |

I picked `x in 12` because these are important decision points when reaching the end of your deck. As for `4 in 30` it's to represent a "poor" deck 2.

**Insights**
- The chances of hitting brainstorm 4 on deck 1 is basically a coinflip, while the odds increased significantly in your favor in deck 2 (over 40% more likely).
- Even in a "poor" deck 2 the chances of hitting a brainstorm 4 is still close to a coinflip. This also shows how strong deck 2 compression is.
- For all you double brainstorm enjoyers out there the chances to whiff on deck 1 is more than 20%, that means that you'll whiff approximately once every 5 games. Conversely, on deck 2 the chance to whiff is actually not that low at 5.5%, that's almost the double the rate of hitting an SSR in UmaMusume, beware!
- Brainstorm 5 gains significant value over brainstorm 4 in deck 2, with the chances of hitting 2 or more cxs being slightly above 40% vs 30%. That's a third more likely!

## Mill (cx) {#mill}
Chances of being out 4 cxs going first, going second
Chances of drawing the correct cx by turn 2 going first, going second

## Plussing Zeros {#plussing-zeros}
There are several probability-based plussing zeros in Weiss such as aqua rikis & coinflips & avatar salami
