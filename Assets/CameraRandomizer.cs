using UnityEngine;
using UnityEngine.Perception.Randomization.Randomizers;
using System;
using UnityEngine.Perception.Randomization.Parameters;

[Serializable]
[AddComponentMenu("Perception/Randomizer/CameraRandomizer")]
public class CameraRandomizer :Randomizer
{
    public GameObject camera;

   

    protected override void OnIterationStart()
    {
        var taggedObjects=tagManager.Query<CameraRandomizerTag>();
        foreach(var tag in taggedObjects)
        {
            float pitch=UnityEngine.Random.Range(0f,90f);
            float yaw=UnityEngine.Random.Range(0f,360f);
            float dist=UnityEngine.Random.Range(8,20);

            Vector3 randomDirection = Quaternion.Euler(-pitch, yaw, 0f) * Vector3.forward;
            camera.transform.position = tag.transform.position + randomDirection * dist; 

            camera.transform.LookAt(tag.transform);  // tagı tanka eklıyoruz tagımız yanı tankdır burada.
            Debug.Log($"dist: {dist}, camPos: {camera.transform.position}, tankPos: {tag.transform.position}");
        }
    }
}
