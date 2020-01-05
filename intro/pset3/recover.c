#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    FILE *raw_file = fopen(argv[1], "r");
    if(raw_file == NULL)
    {
        fprintf(stderr, "image file can not be opened\n");
        return 2;
    }

    int newImg = 0;
    int found = 0;
    int count = -1;
    char filename[8];
    FILE *img = NULL;
    uint8_t buffer[512];
    long pos = 0;
    while (fread(buffer, 1, 512, raw_file) == 512)
    {
        if(count >= 1)
            fseek(raw_file, -pos, SEEK_CUR);
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            newImg = 1;
            count++;
        }
        else
            newImg = 0;

        if (newImg == 1 && found == 0)
        {
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");
            fwrite(buffer, 1, 512, img);
            found = 1;
            continue;
        }
        else if (newImg == 0 && found == 1)
        {
            fwrite(buffer, 1, 512, img);
        }
        else if (newImg == 1 && found == 1)
        {
            fclose(img);
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");
            fwrite(buffer, 1, 512, img);
        }
        pos = ftell(raw_file);
    }
    fclose(img);

    return 0;
}