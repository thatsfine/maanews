//
//  TableViewController.swift
//  MathNews
//
//  Created by cs laptop on 2/16/16.
//  Copyright (c) 2016 cs121MathNewApp. All rights reserved.
//

import UIKit
import Firebase
//check to see if username works

class TableViewController: UITableViewController {
    //MARK: Properties
    var articles = [String]()
    var articleContent = [String]()
    
    func loadSampleArticles(){
        let link1 = "Secret to the perfect pancake described mathematically"
       
        let content1 = "Maths students from the University of Sheffield have swapped calculus for the kitchen by developing a formula to prepare the perfect pancake."
        let link2 = "Corals, crochet and the cosmos:how hyperbolic geometry pervades the universe"
    
        let content2 = " We have built a world of largely straight lines – the houses we live in, the skyscrapers we work in and the streets we drive on our daily commutes."
        let link3 = "The Intriguing Math That Turns Manhattan Properties Into Shekels"
        
        let content3 = "What do Israeli investors know about retirement homes in Indiana? Enough to lend them $68 million.Strawberry Fields, a real estate investment trust whose facilities cater to Alzheimer’s sufferers in the Midwest, is the latest of at least 14 U.S. property companies that have borrowed a combined 8.1 billion shekels ($2.07 billion) in the Israeli market since 2008, securing interest rates they could only dream of at home."
        //the titles
        articles+=[link1,link2,link3]
        //the content
        articleContent+=[content1,content2,content3]
        
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let ref = Firebase(url:"https://crackling-torch-4312.firebaseio.com")
        // Retrieve new posts as they are added to your database
        ref.observeEventType(.ChildAdded, withBlock: { snapshot in
            print(snapshot.value.objectForKey("KCIVooi4bqdPPIGZN2l"))
            print(snapshot.value.objectForKey("title"))
        })

        //load the sample articles
        loadSampleArticles()

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // Return the number of sections.
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return articles.count
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentfier = "ArticleTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentfier, forIndexPath: indexPath) as!ArticleTableViewCell

        // Configure the cell...
        //title
        cell.LinkLabel?.text = articles[indexPath.row]
        
        //mini-content
        cell.ContentLabel?.text = articleContent[indexPath.row]
        
        

        return cell
    }
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        NSLog("You selected cell #\(indexPath.row)!")
       //opens the url to article depending on the cell that is clicked
        if(indexPath.row == 0){
            UIApplication.sharedApplication().openURL(NSURL(string: "http://phys.org/news/2016-02-secret-pancake-mathematically.html")!)}
        else if (indexPath.row==1){
            UIApplication.sharedApplication().openURL(NSURL(string: "http://phys.org/news/2016-01-corals-crochet-cosmos-hyperbolic-geometry.html")!)
        }
        else{
            UIApplication.sharedApplication().openURL(NSURL(string: "http://www.bloomberg.com/news/articles/2016-02-15/the-intriguing-math-that-turns-manhattan-properties-into-shekels")!)
        }
    }
    
    //


    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using [segue destinationViewController].
        // Pass the selected object to the new view controller.
    }
    */
    
}
