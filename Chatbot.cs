using UnityEngine;
using UnityEngine.Networking;

public class Chatbot : MonoBehaviour
{
    public string apiUrl = "http://localhost:5000/chat";
    public Animator botAnimator;

    public void SendMessageToAI(string userMessage)
    {
        StartCoroutine(PostRequest(apiUrl, userMessage));
    }

    IEnumerator PostRequest(string url, string message)
    {
        WWWForm form = new WWWForm();
        form.AddField("message", message);

        using (UnityWebRequest www = UnityWebRequest.Post(url, form))
        {
            yield return www.SendWebRequest();

            if (www.result == UnityWebRequest.Result.Success)
            {
                string reply = www.downloadHandler.text;
                Debug.Log("Bot reply: " + reply);
                // Wywołaj funkcję animacji mowy
                botAnimator.SetTrigger("Talk");
            }
            else
            {
                Debug.LogError("Error: " + www.error);
            }
        }
    }
}
