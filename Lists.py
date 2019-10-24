{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Hello', [1, 2, 3], 345, 474]\n",
      "9745\n",
      "25\n",
      "[345, 9745, 25, 228.5, 140.09, 'hi', '56', '590']\n",
      "['590', '56', 'hi', 140.09, 228.5, 25, 9745, 345]\n"
     ]
    }
   ],
   "source": [
    "learning = [\"Hello\", [1, 2, 3], 345, 474]\n",
    "print(learning)\n",
    "learning.remove([1, 2, 3])\n",
    "learning.pop()\n",
    "learning.append(9745)\n",
    "learning.append(25)\n",
    "learning.append(228.5)\n",
    "learning.append(140.09)\n",
    "learning.remove(\"Hello\")\n",
    "print(max(learning))\n",
    "print(min(learning))\n",
    "\n",
    "learning2 = ['hi', '56', '590']\n",
    "x = learning + learning2\n",
    "\n",
    "print(x)\n",
    "x.reverse()\n",
    "print(x)"
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
