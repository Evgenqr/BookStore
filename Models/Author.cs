using System.Xml.Linq;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace BookStore.Models
{
    public class Author: BaseEntity
    {
        /// <summary>
        /// ФИО автора
        /// </summary>
        [Required]
        [Display(Name = "ФИО автора")]
        [MaxLength(100)]
        public string FullName { get; set; }
        /// <summary>
        /// Дата рождения автора
        /// </summary>
        [Required]
        [Display(Name = "Дата рождения")]
        [DataType(DataType.Date)]
        [DisplayFormat(DataFormatString = "{0:yyyy-MM-dd}", ApplyFormatInEditMode = true)]
        public DateTime DateOfBirth { get; set; }
        /// <summary>
        /// Литературные жанры автора
        /// </summary>
        public List<Genre> AuthorGenres { get;  } = new List<Genre> ();
     }
}
