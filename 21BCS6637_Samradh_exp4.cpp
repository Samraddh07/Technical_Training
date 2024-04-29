#include <iostream>

using namespace std;

class SinglyLinkedListNode {
public:
    int data;
    SinglyLinkedListNode* next;
    SinglyLinkedListNode(int node_data) {
        this->data = node_data;
        this->next = nullptr;
    }
};

SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* llist,int data) {
    SinglyLinkedListNode* newNode = new SinglyLinkedListNode(data);

    if (llist == nullptr) {
        return newNode;
    } else {
        newNode->next = llist;
        return newNode;
    }
}

void printLinkedList(SinglyLinkedListNode* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    int n, data;
    cout << "Enter the number of elements to be inserted at the head: ";
    cin >> n;
    SinglyLinkedListNode* head = nullptr;
    for (int i = 0; i < n; i++) {
        cout << "Enter the element to be inserted: ";
        cin >> data;
        head = insertNodeAtHead(head, data);
    }
    cout << "Linked List after insertion: ";
    printLinkedList(head);
    return 0;
}