/**
 * Note: The returned array must be allocated using malloc.
 * The caller is responsible for freeing the returned array.
 */
int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int length = strlen(seq);
    int* answer = (int*)malloc(length * sizeof(int));
    int currentGroup = 1;

    *returnSize = length;

    for (int index = 0; index < length; index++) {
        if (seq[index] == '(') {
            answer[index] = 1 - currentGroup;
        } else {
            answer[index] = currentGroup;
        }

        currentGroup ^= 1;
    }

    return answer;
}