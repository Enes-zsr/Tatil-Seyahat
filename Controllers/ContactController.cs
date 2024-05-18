using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using SeyahatProje.Models.Sınıflar;
namespace SeyahatProje.Controllers
{
    public class ContactController : Controller
    {
        // GET: Contact
        Context c = new Context();
        İletişim i = new İletişim();

        [HttpGet]
        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Index(İletişim y)
        {
            c.iletişims.Add(y);
            c.SaveChanges();
            return View();
        }

    }
}