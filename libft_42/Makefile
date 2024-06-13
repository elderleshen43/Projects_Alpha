NAME = libft.a

SRCS := ft_atoi.c ft_bzero.c ft_calloc.c ft_isalpha.c ft_isalnum.c ft_isascii.c ft_isdigit.c\
ft_isprint.c ft_itoa.c ft_memchr.c ft_memcmp.c ft_memcpy.c ft_memmove.c ft_memset.c\
ft_putchar_fd.c ft_putendl_fd.c ft_putnbr_fd.c ft_putstr_fd.c ft_split.c ft_strdup.c ft_strchr.c\
ft_striteri.c ft_strjoin.c ft_strlcat.c ft_strlcpy.c ft_strlen.c\
ft_strmapi.c ft_strncmp.c ft_strnstr.c ft_strrchr.c ft_strtrim.c ft_substr.c ft_tolower.c ft_toupper.c

SRCS_B = ft_lstadd_front.c ft_lstadd_back.c	 ft_lstnew.c ft_lstsize.c ft_lstlast.c\
		ft_lstdelone.c ft_lstclear.c ft_lstiter.c ft_lstmap.c

OBJS = $(SRCS:.c=.o)
OBJS_B = $(SRCS_B:.c=.o)

FLAGS := -Wall -Wextra -Werror

CC = cc

HEADER := libft.h	

%.o : %c
		gcc $(FLAGS) -c $< I$(HEADER) -o $@
		
bonus: $(OBJS) $(OBJS_B)
		ar rc $(NAME) $(OBJS) $(OBJS_B)

$(NAME) : $(OBJS)
		ar rcs $(NAME) $(OBJS)
		ranlib $(NAME)

all : $(NAME)

so:
	$(CC) -nostartfiles -fPIC $(FLAGS) $(SRCS) $(SRCS_B)
	gcc -nostartfiles -shared -o libft.so $(OBJS) $(OBJS_B)

clean:
	rm -f $(OBJS)
	rm -f $(OBJS_B)
fclean: clean
		rm -f $(NAME)

re: fclean all

.PHONY: clean fclean re
