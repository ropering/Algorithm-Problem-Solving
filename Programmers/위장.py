{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 63,
   "source": [
    "def solution(clothes):\r\n",
    "    type = 1 # 종류\r\n",
    "    name = 0 # 옷 이름 \r\n",
    "    dic = dict()\r\n",
    "    result = 1\r\n",
    "    for cloth in clothes: # 딕셔너리 선언 및 초기화\r\n",
    "        dic[cloth[1]] = [True] # 순열 식 때문에 key 마다 값 추가\r\n",
    "    \r\n",
    "    for cloth in clothes: # 딕셔너리 값 추가\r\n",
    "        dic[cloth[type]].append(cloth[name])\r\n",
    "    \r\n",
    "    for case in dic.values():\r\n",
    "        result *= len(case)\r\n",
    "    print(dic)\r\n",
    "    return result - 1\r\n",
    "\r\n",
    "solution([[\"yellowhat\", \"headgear\"], [\"bluesunglasses\", \"eyewear\"], [\"green_turban\", \"headgear\"]])"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "{'headgear': [True, 'yellowhat', 'green_turban'], 'eyewear': [True, 'bluesunglasses']}\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "execution_count": 63
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [],
   "outputs": [],
   "metadata": {}
  }
 ],
 "metadata": {
  "orig_nbformat": 4,
  "language_info": {
   "name": "python",
   "version": "3.8.6",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.6 64-bit (system)"
  },
  "interpreter": {
   "hash": "2db524e06e9f5f4ffedc911c917cb75e12dbc923643829bf417064a77eb14d37"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}