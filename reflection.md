# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game appeared as a streamlit app titled "Game Glitch Investigator" with a sidebar for settings. It featured a simple input field for guesses and a "Developer Debug Info" expandable dropdown. The game also included a "Submit Guess" button and a "New Game" button.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1: The blue text area is showing that I have the attempts I have left is 1 less than the attempts allowed.
  2: When I submit a guess that's lower than the secret number, the hint tells me to go lower instead of higher, and tells me to go higher when I submit a guess that's higher than the secret number. So the hints are backwards.
  3: Attempts left does not decrement after submitting the first guess.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  For this project, I am using GitHub Copilot because I have the student developer pack. I only have experience using Copilot and never used Claude or Gemini for coding. But I will try out the other AI tools and try to get familiar with them in the future projects.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
