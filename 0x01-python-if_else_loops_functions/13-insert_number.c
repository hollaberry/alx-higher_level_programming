#include "lists.h"
/**
 * insert_node - function pointer to insert a new node
 * @head: head of list
 * @number: new number to be inserted
 * Return: Address of new node or null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *newnode = NULL;
listint_t *temp = NULL;

if (!head)
return (NULL);

newnode = malloc(sizeof(listint_t));
if (!newnode)
return (NULL);
newnode->n = number;
newnode->next = NULL;

if (!*head || (*head)->n > number)
{
newnode->next = *head;
return (*head = newnode);
}
else
{
while (current && current->n < number)
{
temp = current;
current = current->next;
}
temp->next = newnode;
newnode->next = current;
}

return (newnode);
}
