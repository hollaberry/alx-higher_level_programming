#include "lists.h"

/**
 * check_cycle - function to check if a linked list has a cycle
 * @list: pointer to the list
 * Return: True if cycle exist or false if not
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;
if (!list)
{
return (0);
}
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
return (1);
}

}
return (0);
}
