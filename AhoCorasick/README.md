Aho-Corasic多模匹配算法

AC自动机，Aho-Corasick automaton，该算法在1975年产生于贝尔实验室，是著名的多模匹配算法。要学会AC自动机，我们必 须知道什么是Trie，也就是字典树。Trie树，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。

中文：
https://github.com/liu-nlper/AhoCorasickAutomation

```python
#!/usr/bin/env python
# -*-coding:utf-8-*-

import queue


class Match(object):

  def __init__(self, start, end, keyword, w_type):
    self.start = start
    self.end = end
    self.keyword = keyword
    self.w_type = w_type

  def __str__(self):
    return_str = "{0}:{1}={2}".format(self.start, self.end, self.keyword)
    if self.w_type:
        return_str += '/{0}'.format(self.w_type)
    return return_str

  __repr__ = __str__


class State(object):

  def __init__(self, word, deepth):
    self.success = {}
    self.failure = None
    self.emits = dict()
    self.deepth = deepth

  def add_word(self, word):
    if word in self.success:
      return self.success.get(word)
    else:
      state = State(word, self.deepth + 1)
      self.success[word] = state
    return state

  def add_one_emit(self, keyword, value):
    self.emits[keyword] = value

  def add_emits(self, emits):
    if not isinstance(emits, dict):
      raise Exception("keywords need a dict")
    self.emits.update(emits)

  def set_failure(self, state):
    self.failure = state

  def get_transitions(self):
    return self.success.keys()

  def next_state(self, word):
    return self.success.get(word)


class Trie(object):

  def __init__(self, words=None):

    self.root = State("", 0)
    self.root.set_failure(self.root)
    self.is_create_failure = False
    if words:
      self.create_trie(words)

  def create_trie(self, words):
    if isinstance(words, list):
      self.create_trie_from_list(words)
    elif isinstance(words, dict):
      self.create_trie_from_dict(words)
    return self

  def create_trie_from_list(self, keywords):
    for keyword in keywords:
      self.add_keyword(keyword, '')
    self.create_failure()
    return self

  def create_trie_from_dict(self, keywords):
    for keyword, value in keywords.items():
      self.add_keyword(keyword, value)
    self.create_failure()
    return self

  def add_keyword(self, keyword, value):
    current_state = self.root
    word_list = list(keyword)

    for word in word_list:
      current_state = current_state.add_word(word)
    current_state.add_one_emit(keyword, value)

  def create_failure(self):
    root = self.root
    state_queue = queue.Queue()

    for k, v in self.root.success.items():
      state_queue.put(v)
      v.set_failure(root)

    while (not state_queue.empty()):

      current_state = state_queue.get()
      transitions = current_state.get_transitions()

      for word in transitions:
        target_state = current_state.next_state(word)

        state_queue.put(target_state)
        trace_state = current_state.failure

        while trace_state.next_state(word) is None and trace_state.deepth != 0:
          trace_state = trace_state.failure

        if trace_state.next_state(word) is not None:
          target_state.set_failure(trace_state.next_state(word))
          target_state.add_emits(trace_state.next_state(word).emits)
        else:
          target_state.set_failure(trace_state)
    self.is_create_failure = True

  def get_state(self, current_state, word):
    new_current_state = current_state.next_state(word)

    while new_current_state is None and current_state.deepth != 0:
      current_state = current_state.failure
      new_current_state = current_state.next_state(word)

    return new_current_state

  def parse_text(self, text, allow_over_laps=True):
    matchs = []
    if not self.is_create_failure:
      self.create_failure()

    position = 0
    current_state = self.root
    for word in list(text):
      position += 1
      current_state = self.get_state(current_state, word)
      if not current_state:
        current_state = self.root
        continue
      for mw in current_state.emits:
        m = Match(
            position - len(mw), position, mw, w_type=current_state.emits[mw])
        matchs.append(m)
    # todo remove over laps
    return matchs


def create_trie(words):
  return Trie().create_trie(words)


```


```python
#!/usr/bin/env python
# -*-coding:utf-8-*-

from trie import Trie


def demo_list():
  words = ["北京", "故宫", "北京故宫", "中国", "紫禁城"]
  tree = Trie().create_trie_from_list(words)
  text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
  matchs = tree.parse_text(text)
  print(matchs)


def demo_dict():
  words = {"北京": "GPE", "故宫": "LOC", "北京故宫": "LOC", "紫禁城": "LOC"}
  tree = Trie().create_trie_from_dict(words)
  text = "北京故宫是中国明清两代的皇家宫殿，旧称紫禁城。"
  matchs = tree.parse_text(text)
  print(matchs)


if __name__ == '__main__':
  demo_list()

  demo_dict()


```

其他参考：

https://github.com/Guangyi-Z/py-aho-corasick

https://github.com/Superchen17/Aho-Corasick
