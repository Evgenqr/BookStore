using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;

namespace BookStore.Models
{
    public class Book: BaseEntity
    {
        /// <summary>
        /// Id автора
        /// </summary>
        [Required]
        public long AuthorId { get; set; }
        /// <summary>
        /// Автор книги
        /// </summary>
        public Author Author { get; set; }
        /// <summary>
        /// Название книги
        /// </summary>
        [Required]
        [Display(Name = "Название книги")]
        public string Title { get; set; }
        /// <summary>
        /// Описание книги
        /// </summary>
        [Display(Name = "Описание")]
        [MaxLength(1000)]
        public string Description { get; set; }
        /// <summary>
        /// Id жанра книги
        /// </summary>
        [Required]
        public long GenreId { get; set; }
        /// <summary>
        /// Жанр книги
        /// </summary>
        public Genre Genre { get; set; }
        /// <summary>
        /// Год издания книги
        /// </summary>
        [Required]
        public short Year { get; set; }
    }
}
