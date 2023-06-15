using System.ComponentModel.DataAnnotations;

namespace BookStore.Models
{
    public class Genre: BaseEntity
    {
        /// <summary>
        /// Название жанра
        /// </summary>
        [Required]
        [Display(Name = "Название жанра")]
        [MaxLength(100)]
        public string GenreName { get; set; }
        //// <summary>
        //// Авторы, которые связаны с жанром
        //// </summary>
        public List<Author> GenreAuthors { get; } = new List<Author>();
    }
}
