class MyStack {
    Queue<Integer> queue ;
    public MyStack() {
        queue = new LinkedList<>();
    }
    
    public void push(int x) {
        queue.add(x);
        for(int i=0;i<queue.size()-1;i++){
            queue.add(queue.poll());
        }
        
    }
    
    public int pop() {
        int q = queue.poll();
        return q;
    }
    
    public int top() {
        int q = queue.peek();
        return q;
    }
    
    public boolean empty() {
        if(queue.isEmpty()){
            return true;
        }
        return false;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */