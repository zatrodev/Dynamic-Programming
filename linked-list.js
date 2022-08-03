class Node {
    constructor(data = null, prev = null, next = null, top = null, bot = null) {
        this.data = data;
        this.prev = prev;
        this.next = next;
        this.top = top;
        this.bot = bot;
        this.topRight = null;
        this.topLeft = null;
        this.botRight = null;
        this.botLeft = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;

        // questionable
        return new Proxy(this, {
            get(target, prop) {
                if (Number(prop) == prop && !(prop in target)) {
                    return this.data[prop];
                }
                return target[prop];
            },
        });
    }

    add(node) {
        if (this.size === 0) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail.next.prev = this.tail;
            this.tail = this.tail.next;
        }

        this.size++;
        let rowLength = matrix[0].length;

        if (
           this.size % rowLength === 0 &&
            this.size !== 0 &&
            this.size != matrix[0].length
        ) {
            let curr = this.head;
            let bot = this.head;
            let top = this.tail;

            while (rowLength--) {
                bot = bot.next;
                top = top.prev;
            }

            // botStop and topStop indicates where
            // the traversing of nodes should stop
            const botStop = top;
            const topStop = bot;

            // in here, curr is at the first element of a specifc iterating array from the 2D array
            // while botStop is at the last element of the current iterating array
            // for example: 
            // [
            //     [4, 0, 1],
            //     [3, 5, 2]
            // ]
            // in this example, only one iteration will occur since there are only two arrays
            // so, in here, curr is at element 4
            // while botStop is at element 1
            while (curr !== botStop) {
                // bottom of curr (element 4) is bot which is element 3
                curr.bot = bot;

                if (curr.bot.next !== null)
                    curr.botRight = curr.bot.next;
                if (curr.bot.prev !== null)
                    curr.botLeft = curr.bot.prev;

                // traverse until botStop
                curr = curr.next;
                bot = bot.next;
            }


            // same goes here, just reversed
            curr = this.tail;

            while (curr !== topStop) {
                curr.top = top;

                if (curr.top.next !== null)
                    curr.topRight = curr.top.next;
                if (curr.top.prev !== null)
                    curr.topLeft = curr.top.prev;
                    
                curr = curr.prev;
                top = top.prev;
            }
        }
    }
}

let matrix = [
    [4, 0, 1],
    [3, 5, 2],
];

function arrayToLinkedList(matrix) {
    let nodeArray = new LinkedList();

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            try {
                nodeArray.add(
                    new Node(
                        matrix[i][j],
                        new Node(matrix[i][j - 1]),
                        new Node(matrix[i][j + 1]),
                        new Node(matrix[i - 1][j]),
                        new Node(matrix[i + 1][j])
                    )
                );
            } catch {
                let node = new Node(matrix[i][j]);
                if (j - i >= 0) 
                    node.prev = new Node(matrix[i][j - 1]);
                if (j + 1 < matrix[i].length)
                    node.next = new Node(matrix[i][j + 1]);
                if (i - 1 >= 0) 
                    node.top = new Node(matrix[i - 1][j]);
                if (i + 1 > matrix.length)
                    node.bot = new Node(matrix[i + 1][j]);

                nodeArray.add(node);
            }
        }
    }

    return nodeArray;
}

let nodeArray = arrayToLinkedList(matrix);

console.log(nodeArray.size);
console.log(nodeArray.tail.topRight.data);
