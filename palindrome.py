{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter word/number python\n",
      "it is not a palindrome\n"
     ]
    }
   ],
   "source": [
    "string = input(\"enter word/number \")\n",
    "reverse_string = reversed(string)\n",
    "if list(string) == list(reverse_string):\n",
    "    print(\"it is a palindrome\")\n",
    "else:\n",
    "    print(\"it is not a palindrome\")"
   ]
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
