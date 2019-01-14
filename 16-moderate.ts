// 16.1 Number Swapper

// What is this asking?

// 16.2 Word Frequencies

// if we only need to do this once we can do it  on the fly in constant time because the length of the word is much smalle3r than the length of the book (linear to the book)

function oneOffFrequency(book: string, word: string): number {
  return book.split(word).length - 1
}

// but if we are going to be doing this a lot we can preprocess all the words into a trie and look up words in linear time relative to their word lenght instead of the books length

function defaultTrie(): Trie {
  return {count: 0, children: {}} as Trie
}

interface Trie {
  count: number
  children: {[c in string]: Trie|undefined}
}

function countWord(trie: Trie, word: string) {
  if (word === '') {
    trie.count += 1
    return
  }

  if (!trie.children[word[0]]) {
    trie.children[word[0]] = defaultTrie()
  }

  countWord(trie.children[word[0]], word.slice(1)) // could use a pointer to the char instead of slicing if this is too expensive.  This is more readable though and we are preprocessing this
}


function storeAsTrie(book: string): Trie {
  const words = book.split(/(\s)|(?)|(\!)/)

  const trie = defaultTrie()

  words.forEach(word => countWord(trie, word))

  return trie
}

function countWordMemoized(trie: Trie, word: string) {
  if (word === '') {
    return trie.count
  }
  if (!trie.children[word[0]]) {
    return 0
  }
  return countWordMemoized(trie.children[word[0]], word.slice(1)) // can use a pointer if this is too expensive
}


// 16.3 Intersection


interface GraphPoint {
  x: number,
  y: number,
}

interface LineSegment {
  start: GraphPoint,
  end: GraphPoint,
}

// TODO make not private
interface _MB { // y = mx + b
  m: number,
  b: number,
}

function findIntersection(l1: LineSegment, l2: LineSegment): GraphPoint|_MB|null {

  function getMxb(ls: LineSegment): _MB {
    const m = ((ls.start.y - ls.end.y) ** 2) / ((ls.start.x - ls.end.x) ** 2)
    const b = ls.start.y - m * ls.start.x
    return {m, b}
  }

  function getIntersection(mb1: _MB, mb2: _MB): GraphPoint|_MB|null {
    if (mb1.m === mb2.m ) {
      return mb1.b === mb2.b
        ? mb1
        : null
    }
    const x = (mb2.b - mb1.b) / (mb1.m - mb2.m)
    const y = mb1.m * x + mb1.b

    return {x, y} as GraphPoint
  }

  function isMX(x: any): boolean {
    return (intersection as any).m && (intersection as any).b
  }

  function isOnLine(point: GraphPoint, line: LineSegment): boolean {
    return (
      ((line.start.x < point.x && point.x < line.end.x) || (line.end.x < point.x) && (point.x < line.start.x)) &&
      ((line.start.y < point.y) && (point.y < line.end.y) || (line.end.y < point.y) && (point.y < line.start.y))
    )
  }

  const intersection = getIntersection(getMxb(l1), getMxb(l2))

  if (intersection === null) {
    return null
  }

  if (isMX(intersection)) {
    return intersection as _MB // could return actual segment instead
  }

  const graphPointIntersection = intersection as GraphPoint

  if (!isOnLine(graphPointIntersection, l1) || !isOnLine(graphPointIntersection, l2)) {
    return null
  }

  return graphPointIntersection
}


