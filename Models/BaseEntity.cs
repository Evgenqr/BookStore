using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BookStore.Models
{
    /// <summary>
    /// Базовая сущность с идентификатором
    /// </summary>
    public class BaseEntity : IEntity, IHaveId
    {
        object IEntity.Id
        {
            get
            {
                return Id;
            }
            set
            {
                Id = (long)value;
            }
        }
        /// <summary>
        /// Идентификатор
        /// </summary>
        [Display(Name = "Идентификатор")]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public virtual long Id { get; set; }
    }
}
