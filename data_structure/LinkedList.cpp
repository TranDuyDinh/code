#include <iostream>
// #include <memory>
using namespace std;

struct Node
{
    int value;
    std::shared_ptr<Node> next;
    Node(int v) : value(v), next(nullptr) {}
};

void append(Node &head, int d){
    Node* n = &head;    
    while(n->next != nullptr){
            n = n->next.get();
    }
    n->next = std::make_shared<Node>(d);
}

int main() {
    Node head(0);
    for(int i=1;i<5;i++){
            append(head, i);
    }    
    Node n = head;
    while(n.next != nullptr){
            cout << n.value<<" ";
            n = *n.next;
    }
    cout<<n.value<<endl;

    cout << "\nGoodbye..." << endl;
    return 0;
}
