using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BookStore.Models
{
    //Базовая сущность с идентификатором
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
        //Идентификатор
        [Display(Name = "Идентификатор")]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public virtual long Id { get; set; }
    }
}
