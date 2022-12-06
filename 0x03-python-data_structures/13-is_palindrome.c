#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

typedef struct listint {
  int n;
  struct listint *next;
} listint_t;
/**
  * is_palindrome - A function that checks if a list is a palindrome.
  * @head: The pointer to the head of the list.
  * Return: 0 if list not a palindrome, 1 if it is.
  */

int is_palindrome(listint_t **head) {
  // Handle empty list
  if (*head == NULL) {
    return 1;
  }

  // Find the middle of the list
  listint_t *slow = *head;
  listint_t *fast = *head;
  while (fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;
  }

  // Reverse the second half of the list
  listint_t *prev = NULL;
  listint_t *curr = slow;
  while (curr != NULL) {
    listint_t *next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  // Compare the first and second half of the list
  listint_t *left = *head;
  listint_t *right = prev;
  while (right != NULL) {
    if (left->n != right->n) {
      return 0;
    }
    left = left->next;
    right = right->next;
  }

  // Restore the original list
  curr = prev;
  prev = NULL;
  while (curr != NULL) {
    listint_t *next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  return 1;
}

