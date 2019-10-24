{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n"
     ]
    }
   ],
   "source": [
    "def sumList(x):\n",
    "    total = 0\n",
    "    for i in x:\n",
    "        total = total + i\n",
    "    return total\n",
    "print(sumList([2, 4, 5, 7]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28\n"
     ]
    }
   ],
   "source": [
    "def MyMax(x, y):\n",
    "    if x > y:\n",
    "        print(x)\n",
    "    else:\n",
    "        print(y)\n",
    "MyMax(9, 28)       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "def MyMin(x, y):\n",
    "    if x < y:\n",
    "        print(x)\n",
    "    else:\n",
    "        print(y)\n",
    "MyMin(9, 28)       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mourice Otieno Oduor\n",
      "Mourice \n",
      "Otieno \n",
      "Oduor\n"
     ]
    }
   ],
   "source": [
    "def MyName(name1,  name2,  name3):\n",
    "    MyName = name1 + name2 + name3\n",
    "    print(MyName)\n",
    "    \n",
    "MyName('Mourice ','Otieno ', 'Oduor')\n",
    "MyName('Mourice \\n','Otieno \\n', 'Oduor')"
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
