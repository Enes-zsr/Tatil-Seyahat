using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using System.Data.Entity;
namespace SeyahatProje.Models.Sınıflar
{
    public class Context : DbContext

    {
        public virtual DbSet<Admin> Admins { get; set; }
        public virtual DbSet<AdresBlog> AdresBlogs { get; set; }
        public virtual DbSet<Blog> Blogs { get; set; }
        public virtual DbSet<Hakkımızda> Hakkımızdas { get; set; }
        public virtual DbSet<İletişim> iletişims { get; set; }
        public virtual DbSet<Yorumlar> Yorumlars { get; set; }
        public virtual DbSet<TarihiYerler>tarihiYerlers { get; set; }
        public virtual DbSet<DogalGuzellikler>DogalGuzellikler { get; set; }




    }
}