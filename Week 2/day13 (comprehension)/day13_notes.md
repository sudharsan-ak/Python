# Day 13 Notes - Comprehensions

Status: Cleared

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## What Day 13 covered

Day 13 used Asabeneh's List Comprehension day as the backbone, but the lesson was expanded into **comprehensions** more broadly. The goal was to learn Python properly instead of only following the roadmap title.

Topics covered:

```text
list comprehension basics
normal loop vs comprehension
number transformations with range()
filtering with if
transform + filter together
if / else inside comprehension
nested list comprehension / flattening
dictionary comprehension
set comprehension
generator expression awareness
tuple comprehension clarification
light lambda awareness
final mixed exercise
```

## 1. List comprehension basics

A list comprehension creates a new list from an iterable.

```python
new_list = [expression for item in iterable]
```

Example:

```python
languages = ["Python", "JavaScript", "React", "Node.js"]
language_labels = [f"Learning {language}" for language in languages]
uppercase_languages = [language.upper() for language in languages]
language_lengths = [len(language) for language in languages]
```

Equivalent normal-loop idea:

```python
language_labels = []
for language in languages:
    language_labels.append(f"Learning {language}")
```

JavaScript comparison:

```javascript
const languageLabels = languages.map(language => `Learning ${language}`);
```

Key idea:

```text
List comprehension is a compact way to build a new list.
It does not mutate the original list unless you explicitly reassign something.
```

## 2. Number transformations with range()

Comprehensions can use `range()`.

```python
numbers = [number for number in range(1, 11)]
squares = [number ** 2 for number in range(1, 11)]
cubes = [number ** 3 for number in range(1, 11)]
numbers_plus_ten = [number + 10 for number in range(1, 11)]
number_labels = [f"Number: {number}" for number in range(1, 11)]
```

Reminder:

```text
range(1, 11) gives 1 through 10.
The stop value is excluded.
Use range(1, 11), not range(1,11), for cleaner spacing.
```

## 3. Filtering with if

Filtering keeps only items that match a condition.

```python
new_list = [item for item in iterable if condition]
```

Examples:

```python
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
passing_scores = [score for score in scores if score >= 70]
long_languages = [language for language in languages if len(language) > 5]
```

Substring filtering:

```python
js_related_languages = [
    language for language in languages
    if "Java" in language or "Node" in language
]
```

Avoid the bad `or` pattern:

```python
# Wrong
language == "Java" or "Node"
```

Key idea:

```text
A trailing if skips items that do not match.
```

## 4. Transform + filter together

This keeps matching items and stores a transformed value.

```python
new_list = [transformed_value for item in iterable if condition]
```

Examples:

```python
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
odd_cubes = [number ** 3 for number in numbers if number % 2 != 0]
passing_score_labels = [f"Passing score: {score}" for score in scores if score >= 70]
long_uppercase_languages = [language.upper() for language in languages if len(language) > 5]
```

Mental model:

```text
Loop through items.
Keep only matching items.
Transform the matching items.
Store transformed values in a new list.
```

JavaScript comparison:

```javascript
const evenSquares = numbers
  .filter(number => number % 2 === 0)
  .map(number => number ** 2);
```

## 5. if / else inside list comprehension

Use `if / else` when every item should produce output, but the output depends on a condition.

```python
new_list = [value_if_true if condition else value_if_false for item in iterable]
```

Examples:

```python
number_types = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
score_results = ["Pass" if score >= 70 else "Fail" for score in scores]
formatted_languages = [
    language.upper() if len(language) > 5 else language.lower()
    for language in languages
]
```

Important distinction:

```text
Trailing if = skip some items.
if / else before for = every item produces something.
```

## 6. Nested list comprehension / flattening

Flattening means turning a nested list into one flat list.

```python
weekly_topics = [
    ["Dictionaries", "Conditionals"],
    ["Loops", "Functions"],
    ["Modules", "Comprehensions"]
]
```

Normal nested loop:

```python
all_topics = []
for topic_group in weekly_topics:
    for topic in topic_group:
        all_topics.append(topic)
```

Nested comprehension:

```python
all_topics = [topic for topic_group in weekly_topics for topic in topic_group]
```

Pattern:

```python
[item for inner_list in outer_list for item in inner_list]
```

With transformation/filtering:

```python
uppercase_topics = [topic.upper() for topic_group in weekly_topics for topic in topic_group]
long_topics = [topic for topic_group in weekly_topics for topic in topic_group if len(topic) > 7]
```

Critical rule:

```text
Nested comprehension for-clauses must stay in the same order as normal nested loops.
Do not reorder them.
```

## 7. Dictionary comprehension

Dictionary comprehension creates a dictionary.

```python
new_dict = {key_expression: value_expression for item in iterable}
```

Examples:

```python
square_map = {number: number ** 2 for number in numbers}
language_lengths = {language: len(language) for language in languages}
```

From an existing dictionary, use `.items()`:

```python
score_results = {
    name: "Pass" if score >= 70 else "Fail"
    for name, score in student_scores.items()
}
```

Filtering dictionary entries:

```python
passing_students = {
    name: score
    for name, score in student_scores.items()
    if score >= 70
}
```

Warning:

```text
Dictionary keys must be unique.
If duplicate keys are produced, the later value overwrites the earlier one.
```

## 8. Set comprehension

Set comprehension creates a set.

```python
new_set = {expression for item in iterable}
```

Examples:

```python
unique_languages = {language for language in languages}
unique_language_lengths = {len(language) for language in languages}
first_letters = {tool[0] for tool in tools}
passing_score_set = {score for score in scores if score >= 70}
```

Important distinction:

```text
{value for item in iterable}      -> set comprehension
{key: value for item in iterable} -> dictionary comprehension
```

Set comprehension removes duplicates, and set output order is not dependable.

## 9. Generator expression awareness

A generator expression uses parentheses.

```python
squares_generator = (number ** 2 for number in range(1, 6))
```

This does not create a list or tuple. It creates a generator object.

```text
List comprehension creates all values immediately.
Generator expression produces values lazily when needed.
Generators can be consumed once.
```

Example:

```python
cubes_generator = (number ** 3 for number in range(1, 6))
cubes_from_generator = list(cubes_generator)
```

Generator expressions will be covered more deeply later in an Iterators / Generators addendum.

## 10. Tuple comprehension clarification

Python does not have true tuple comprehension.

```python
numbers_generator = (number for number in range(1, 6))      # generator
numbers_tuple = tuple(number for number in range(1, 6))     # tuple
```

This also works:

```python
numbers_list = [number for number in range(1, 6)]
numbers_tuple = tuple(numbers_list)
```

Mental model:

```text
[] -> list comprehension
{} with one expression -> set comprehension
{} with key: value -> dictionary comprehension
() with comprehension-like syntax -> generator expression
tuple(...) -> creates a tuple from an iterable
```

## 11. Light lambda awareness

A lambda is a small anonymous function.

```python
lambda parameter: expression
```

Examples:

```python
double_number = lambda number: number * 2
add_numbers = lambda first_number, second_number: first_number + second_number
is_passing = lambda score: score >= 70
```

JavaScript comparison:

```javascript
const doubleNumber = number => number * 2;
```

Rule:

```text
Tiny one-expression temporary function -> lambda can be okay.
Named reusable logic -> use def.
Complex logic -> definitely use def.
```

Lambda was only introduced lightly. It should be covered properly in Day 14 - Higher Order Functions.

## What was practiced

Day 13 practice included:

```text
normal loop vs list comprehension
list comprehension from lists and range()
filtering and transform + filter patterns
if / else inside comprehension
nested list flattening
dictionary comprehension from lists and dictionaries
set comprehension and duplicate removal
generator expression creation and consumption
tuple creation with tuple(...)
light lambda usage
```

## Mistakes, prompt mismatches, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| Asked whether list comprehension only works from lists | It works from any iterable: list, tuple, string, range, dictionary, set, etc. The output is a list because of `[]`. |
| Asked whether dictionary/set/tuple comprehensions exist | Dictionary and set comprehensions exist. Tuple comprehension does not; parentheses create a generator expression. |
| Asked whether Day 13 should expand beyond list comprehension | Yes. Day 13 was expanded into comprehensions broadly instead of blindly following the repo title. |
| File split confusion | Final structure used separate files for list, dictionary, set, generator/tuple/lambda awareness, and final exercise. |
| Asked whether filter + transform means transform after filtering | Correct mental model: keep matching items, transform matching items, store transformed values. |
| Asked why `if / else` appears before the `for` | Syntax places conditional expression before `for`, but mentally the loop still processes item by item. |
| Asked what happens if nested comprehension `for` order changes | It fails or becomes wrong because variables are used before they exist; keep the same order as normal nested loops. |
| Topic 10 used `tuple(numbers_generator)` instead of generator expression directly inside `tuple()` | Valid Python and proved the concept; prompt mismatch, not a logic bug. |
| Lambda spacing used `lambda score : score >= 90` | Works, but preferred style is `lambda score: score >= 90`. |
| Long one-line comprehensions | Works, but multi-line formatting is cleaner when comprehensions become long. |
| Trailing spaces in multi-line comprehensions | Not functional bugs, but clean them up for style. |

## Final mixed exercise status

The final mixed exercise used a fresh Python bootcamp analytics cleanup scenario and covered:

```text
list comprehension
filtering
if / else transformation
nested list flattening
dictionary comprehension
set comprehension
generator expression
tuple conversion
light lambda awareness
```

Final file:

```text
day13_final.py
```

Final status:

```text
Cleared
```

## Day 13 key takeaways

```text
List comprehension creates a new list from an iterable.
Use [expression for item in iterable] for basic transformations.
Use [item for item in iterable if condition] for filtering.
Use [transformed for item in iterable if condition] for transform + filter.
Use [true_value if condition else false_value for item in iterable] when every item should produce output.
Trailing if skips items.
if / else before for transforms every item differently.
Nested comprehensions follow the same order as normal nested loops.
Use [item for inner_list in outer_list for item in inner_list] to flatten one level.
Use {key: value for item in iterable} for dictionary comprehension.
Use {expression for item in iterable} for set comprehension.
Set comprehension removes duplicates and has no dependable output order.
Parentheses with comprehension-like syntax create a generator expression.
A generator expression is lazy and can be consumed.
Python does not have true tuple comprehension.
Use tuple(...) to build a tuple from an iterable or generator expression.
Lambda creates a small anonymous one-expression function.
Use lambda lightly; prefer def for reusable or complex logic.
```

## Ready for next day

```text
Day 14 - Higher Order Functions
```
