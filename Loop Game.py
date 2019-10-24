{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your integer from1 to 10:-5\n",
      "number too small\n",
      "Enter your integer from1 to 10:3646\n",
      "number too high\n",
      "Enter your integer from1 to 10:4\n",
      "number too high\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "number = random.randint(1, 10)\n",
    "guess = int(input(\"Enter your integer from1 to 1000:\"))\n",
    "while number!= \"guess\":\n",
    "  if guess < number:\n",
    "     print(\"number too small\")\n",
    "     guess = int(input(\"Enter your integer from1 to 1000:\"))\n",
    "\n",
    "  elif guess > number:\n",
    "    print(\"number too high\")\n",
    "    guess = int(input(\"Enter your integer from1 to 1000:\"))\n",
    "    \n",
    "  elif guess == number:\n",
    "    print(\"you won!\")\n",
    "    \n",
    "    break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
