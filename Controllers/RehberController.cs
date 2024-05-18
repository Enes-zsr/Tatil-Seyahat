using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using SeyahatProje.Models.Sınıflar;

namespace SeyahatProje.Controllers
{
    public class RehberController : Controller
    {
        // GET: Rehber
        Context c= new Context();   

        public ActionResult Index()
        {
            var tarihiyerler=c.tarihiYerlers.ToList();
            return View(tarihiyerler);
        }
        public ActionResult Index2()
        {
            var dogalguzellikler = c.DogalGuzellikler.ToList();
            return View(dogalguzellikler);
        }
    }
}